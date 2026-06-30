% =====================================================================
% Questao 5 - Programacao Algoritmica (Trabalho Octave - Matrizes)
% Le uma matriz 5x4 (5 linhas, 4 colunas) com numeros inteiros e mostra
% o MAIOR numero de cada linha da matriz.
% =====================================================================

clc;
clear;

linhas = 5;
colunas = 4;
M = zeros(linhas, colunas);

% --- Leitura da matriz, elemento a elemento ---
disp('Digite os 20 elementos inteiros da matriz 5x4:');
for i = 1:linhas
  for j = 1:colunas
    M(i, j) = input(sprintf('Elemento (%d,%d): ', i, j));
  end
end

% --- Exibe a matriz lida ---
printf('\nMatriz informada:\n');
disp(M);

% --- Encontra e mostra o maior de cada linha ---
printf('Maior numero de cada linha:\n');
for i = 1:linhas
  maior = M(i, 1);              % assume o primeiro como maior
  for j = 2:colunas
    if M(i, j) > maior
      maior = M(i, j);         % atualiza quando achar um maior
    end
  end
  printf('Linha %d: %d\n', i, maior);
end
