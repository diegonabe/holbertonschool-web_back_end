export default function getResponseFromAPI() {
  // Simula una llamada a API con tiempo de espera
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ data: 'Successfully retrieved data' });
    }, 1000);
  });
}
