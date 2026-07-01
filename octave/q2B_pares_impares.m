% =========================================================
% QUESTAO 2 - ALTERNATIVA B (Judaismo)
% Solicita, atraves de um laco de repeticao, a idade de 16
% judeus que ja receberam a lapide, copiando as idades PARES
% para um vetor e as idades IMPARES para outro vetor.
% Lista na tela os 2 vetores.
% =========================================================

pares   = [];
impares = [];

for i = 1:16
  idade = input(sprintf("Digite a idade do judeu %d: ", i));
  if mod(idade, 2) == 0
    pares(end+1) = idade;
  else
    impares(end+1) = idade;
  end
end

printf("\nVetor de idades PARES:\n");
disp(pares);

printf("\nVetor de idades IMPARES:\n");
disp(impares);
