% =========================================================
% QUESTAO 2 - ALTERNATIVA A (Judaismo)
% Solicita 10 idades de judeus falecidos SEM lapide (vetor 1)
% e 10 idades de judeus que JA receberam a lapide (vetor 2).
% Concatena os 2 vetores em 1 vetor de 20 posicoes, lista o
% novo vetor e escreve a MAIOR idade existente nele.
% =========================================================

semLapide = zeros(1, 10);
comLapide = zeros(1, 10);

printf("--- Idades de judeus que ainda NAO receberam a lapide ---\n");
for i = 1:10
  semLapide(i) = input(sprintf("Digite a idade %d: ", i));
end

printf("\n--- Idades de judeus que JA receberam a lapide ---\n");
for i = 1:10
  comLapide(i) = input(sprintf("Digite a idade %d: ", i));
end

% Concatenacao dos 2 vetores em 1 vetor de 20 posicoes
vetor20 = [semLapide, comLapide];

printf("\nNovo vetor com 20 posicoes:\n");
disp(vetor20);

printf("\nMAIOR idade do vetor: %d\n", max(vetor20));
