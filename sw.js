// Service worker — Guide Clinique IPS
// Stratégie : "réseau en priorité, cache en secours"
// -> Connecté : va toujours chercher la dernière version en ligne, et la met à jour en cache
// -> Hors ligne : sert automatiquement la dernière version mise en cache avec succès

const CACHE_NAME = 'guide-clinique-ips-cache-v1';
const ASSETS_A_METTRE_EN_CACHE = [
  './',
  './index.html'
];

self.addEventListener('install', function (event) {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(function (cache) {
      return cache.addAll(ASSETS_A_METTRE_EN_CACHE);
    })
  );
});

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(
        keys.filter(function (key) { return key !== CACHE_NAME; })
            .map(function (key) { return caches.delete(key); })
      );
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (event) {
  // On ne gère que les requêtes GET (navigation/page)
  if (event.request.method !== 'GET') return;

  event.respondWith(
    fetch(event.request)
      .then(function (response) {
        // Succès réseau -> on met à jour la copie en cache pour un usage hors ligne futur
        var responseCopie = response.clone();
        caches.open(CACHE_NAME).then(function (cache) {
          cache.put(event.request, responseCopie);
        });
        return response;
      })
      .catch(function () {
        // Échec réseau (hors ligne) -> on sert la dernière version connue
        return caches.match(event.request).then(function (cached) {
          return cached || caches.match('./index.html');
        });
      })
  );
});
