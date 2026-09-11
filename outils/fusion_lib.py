# -*- coding: utf-8 -*-
"""Boîte à outils commune aux fusions d'encadrés du guide.

Principe : on ne réécrit pas le contenu, on le redécoupe. Chaque fusion
extrait les morceaux des encadrés d'origine et les remonte dans un ordre
unique, sans rien perdre — la vérification compare les termes clés avant
et après.
"""
import re

P = "/sessions/focused-admiring-hawking/mnt/Guide d'étude HTML/index.html"
TAG = re.compile(r'<(/?)div\b[^>]*>')


def lire():
    return open(P, encoding='utf-8').read()


def ecrire(c):
    open(P, 'w', encoding='utf-8').write(c)


def fin_div(s, i):
    d = 0
    for m in TAG.finditer(s, i):
        d += -1 if m.group(1) else 1
        if d == 0:
            return m.end()
    raise AssertionError('div non fermé en %d' % i)


def bloc(c, bid):
    """(debut_ligne, fin, ouverture, corps) de l'encadré portant l'id bid."""
    i = c.find('id="%s"' % bid)
    assert i > 0, 'encadré %s introuvable' % bid
    st = c.rfind('<div class="block ', 0, i)
    en = fin_div(c, st)
    ligne = c.rfind('\n', 0, st) + 1
    ouv = c[st:c.index('>', st) + 1]
    t_fin = c.index('</div>', c.index('block-title', st)) + len('</div>')
    corps = c[t_fin:c.rfind('</div>', 0, en)]
    return ligne, en, ouv, corps


def morceau(corps, debut, fin=None, inclus=True):
    """Sous-chaîne du corps, de `debut` jusqu'à `fin` (exclu) ou la fin."""
    i = corps.index(debut)
    if fin is None:
        return corps[i:]
    j = corps.index(fin, i)
    return corps[i:j + (len(fin) if inclus else 0)]


def keyfact(corps, couleur, n=0):
    """La n-ième key-fact de la couleur donnée, balise complète."""
    ms = list(re.finditer(r'<div class="key-fact %s"[^>]*>' % couleur, corps))
    assert len(ms) > n, 'key-fact %s #%d absente' % (couleur, n)
    i = ms[n].start()
    return corps[i:fin_div(corps, i)]


def tableau(corps, n=0):
    """Le n-ième conteneur <div style="overflow-x:auto...><table>…</div>."""
    ms = list(re.finditer(r'<div style="overflow-x:auto[^>]*>', corps))
    assert len(ms) > n, 'tableau #%d absent' % n
    i = ms[n].start()
    return corps[i:fin_div(corps, i)]


def grille(corps, n=0):
    """La n-ième grille de cartes pastel."""
    ms = list(re.finditer(r'<div style="display:grid[^>]*>', corps))
    assert len(ms) > n, 'grille #%d absente' % n
    i = ms[n].start()
    return corps[i:fin_div(corps, i)]


def criteres(corps, n=0):
    """La n-ième criteria-list."""
    ms = list(re.finditer(r'<div class="criteria-list"[^>]*>', corps))
    assert len(ms) > n, 'criteria-list #%d absente' % n
    i = ms[n].start()
    return corps[i:fin_div(corps, i)]


def st(titre, couleur='#6d28d9'):
    return ('\n        <div style="font-size:12px;font-weight:800;color:%s;'
            'margin-top:18px;letter-spacing:.4px;">%s</div>\n' % (couleur, titre))


def kf(couleur, contenu, mt=12):
    return '\n        <div class="key-fact %s" style="margin-top:%dpx;">%s</div>\n' % (couleur, mt, contenu)


def titre_bloc(bid, tag, obj):
    return ('        <div class="block-title" id="%s"><span class="tag">%s</span>'
            '<span class="obj-badge">%s</span></div>\n' % (bid, tag, obj))


def fusionner(c, garde, absorbe, ouverture, tag, obj, corps):
    """Remplace l'encadré `garde` par le bloc fusionné et supprime `absorbe`."""
    neuf = '      %s\n%s%s      </div>\n' % (ouverture, titre_bloc(garde, tag, obj), corps)
    spans = []
    for bid in [garde] + absorbe:
        l, e, _, _ = bloc(c, bid)
        spans.append((l, e, bid))
    spans.sort()
    ancre = [s for s, _, b in spans if b == garde][0]
    perdu = sum(e - s for s, e, _ in spans)
    for s, e, _ in sorted(spans, reverse=True):
        c = c[:s] + c[e:]
    # l'ancre se décale si des blocs supprimés la précédaient
    decale = sum(e - s for s, e, b in spans if s < ancre)
    c = c[:ancre - decale] + neuf + c[ancre - decale:]
    return c, perdu, len(neuf)


def nav_supprimer(c, section, ids):
    a = c.find('<div class="section" id="sec-%s"' % section)
    b = c.find('<div class="section" id=', a + 10)
    seg = c[a:b]
    nav = re.search(r'gap:8px;margin-bottom:18px;">(.*?)</div>\s*\n', seg, re.S)
    assert nav, 'barre de navigation introuvable'
    bn = nav.group(1)
    for bid in ids:
        m = re.search(r'\s*<button onclick="goToBlock\(\'%s\'\)".*?</button>' % re.escape(bid), bn, re.S)
        assert m, 'bouton %s introuvable' % bid
        bn = bn[:m.start()] + bn[m.end():]
    seg = seg[:nav.start(1)] + bn + seg[nav.end(1):]
    return c[:a] + seg + c[b:]


def nav_relibeller(c, section, bid, libelle):
    a = c.find('<div class="section" id="sec-%s"' % section)
    b = c.find('<div class="section" id=', a + 10)
    seg = c[a:b]
    m = re.search(r'(<button onclick="goToBlock\(\'%s\'\)"[^>]*>)(.*?)(</button>)' % re.escape(bid), seg, re.S)
    assert m, 'bouton %s introuvable' % bid
    seg = seg[:m.start(2)] + libelle + seg[m.end(2):]
    return c[:a] + seg + c[b:]


MOTS = re.compile(r"[0-9A-Za-zÀ-ÿ']{4,}")


def empreinte(txt):
    """Multiensemble des mots du texte visible — sert à prouver l'absence de perte."""
    t = re.sub(r'<[^>]+>', ' ', txt).lower()
    t = t.replace('&#39;', "'").replace('&amp;', '&').replace('&mdash;', '—').replace('&nbsp;', ' ')
    from collections import Counter
    return Counter(MOTS.findall(t))


def controle(avant_txt, apres_txt, tolere=()):
    a, b = empreinte(avant_txt), empreinte(apres_txt)
    perdu = a - b
    for m in tolere:
        perdu.pop(m, None)
    return perdu
