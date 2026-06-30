% =====================================================================
% Questao 2 - Programacao Algoritmica (Trabalho Octave - Matrizes)
% Le uma matriz M(5x5). Em seguida preenche com 2 a diagonal secundaria
% e com zeros os demais elementos. Mostra a matriz original e a resultante.
% =====================================================================

clc;
clear;

n = 5;                  % matriz 5x5
M = zeros(n, n);

% --- Leitura da matriz, elemento a elemento ---
disp('Digite os 25 elementos da matriz 5x5:');
for i = 1:n
  for j = 1:n
    M(i, j) = input(sprintf('Elemento (%d,%d): ', i, j));
  end
end

% --- Monta a matriz resultante ---
% Diagonal secundaria -> elementos onde i + j = n + 1 (ex.: 5+1 = 6)
R = zeros(n, n);
for i = 1:n
  for j = 1:n
    if (i + j) == (n + 1)
      R(i, j) = 2;      % diagonal secundaria recebe 2
    end
  end
end

% --- Exibe os resultados ---
printf('\nMatriz original:\n');
disp(M);

printf('Matriz resultante (diagonal secundaria = 2, demais = 0):\n');
disp(R);
