% =========================================================
% QUESTAO 3 - ALTERNATIVA B (Catolicismo)
% Le uma matriz quadrada 5x5 com as quantidades de pecados
% que algumas almas chegam ao purgatorio. Mostra a matriz.
% Cria um vetor de 5 posicoes com o TERCEIRO elemento de
% todas as LINHAS e outro vetor de 5 posicoes com o SEGUNDO
% elemento de todas as COLUNAS. Mostra os vetores criados.
% =========================================================

M = zeros(5, 5);

% Leitura da matriz 5x5
for i = 1:5
  for j = 1:5
    M(i, j) = input(sprintf("Quantidade de pecados [linha %d, coluna %d]: ", i, j));
  end
end

printf("\nMatriz 5x5 de pecados:\n");
disp(M);

% Vetor com o terceiro elemento de todas as linhas
vLinhas = zeros(1, 5);
for i = 1:5
  vLinhas(i) = M(i, 3);
end

% Vetor com o segundo elemento de todas as colunas
vColunas = zeros(1, 5);
for j = 1:5
  vColunas(j) = M(2, j);
end

printf("\nVetor com o TERCEIRO elemento de todas as LINHAS:\n");
disp(vLinhas);

printf("\nVetor com o SEGUNDO elemento de todas as COLUNAS:\n");
disp(vColunas);
