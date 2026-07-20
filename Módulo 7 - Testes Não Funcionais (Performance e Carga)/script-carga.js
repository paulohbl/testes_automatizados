// script-carga.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  // Configurando os estágios de Carga:
  stages: [
    { duration: '10s', target: 20 }, // Sobe rápido para 20 usuários
    { duration: '20s', target: 20 }, // Mantém por 20 segundos
    { duration: '5s', target: 0 },   // Retorna a zero
  ],
};

export default function () {
  // Realiza a requisição HTTP GET no endpoint alvo local
  const res = http.get('http://localhost:5000/produtos');
  
  // Realiza "Asserts" para garantir a confiabilidade técnica
  check(res, {
    'Status foi 200 OK': (r) => r.status === 200,
    'A latência foi menor que 500ms': (r) => r.timings.duration < 500,
  });
  
  // Pausa de 0.5s para simular o comportamento humano
  sleep(0.5); 
}
