% =========================================================
% QUESTAO 3 - ALTERNATIVA A (Catolicismo)
% Solicita os valores de uma matriz 6x5 com as quantidades
% de oracoes que um padre fez em um mes. Mostra a matriz.
% Copia os numeros para um vetor de 30 posicoes e mostra o
% vetor. Calcula e escreve o MAIOR, o MENOR e a MEDIA.
% =========================================================

M = zeros(6, 5);

% Leitura da matriz 6x5
for i = 1:6
  for j = 1:5
    M(i, j) = input(sprintf("Quantidade de oracoes [linha %d, coluna %d]: ", i, j));
  end
end

printf("\nMatriz 6x5 de oracoes:\n");
disp(M);

% Copia da matriz para um vetor de 30 posicoes
vetor = zeros(1, 30);
k = 1;
for i = 1:6
  for j = 1:5
    vetor(k) = M(i, j);
    k = k + 1;
  end
end

printf("\nVetor de 30 posicoes:\n");
disp(vetor);

printf("\nMAIOR quantidade de oracoes: %d\n", max(vetor));
printf("MENOR quantidade de oracoes: %d\n", min(vetor));
printf("MEDIA de oracoes: %.2f\n", mean(vetor));
