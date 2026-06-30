% =====================================================================
% Questao 1 - Programacao Algoritmica (Trabalho Octave - Matrizes)
% Le uma matriz M(5x5). Depois preenche com 1 a diagonal principal e
% com zeros os demais elementos. Mostra a matriz original e a resultante.
% =====================================================================

clc;            % limpa a tela
clear;          % limpa as variaveis

n = 5;                  % matriz 5x5
M = zeros(n, n);        % aloca a matriz original

% --- Leitura da matriz, elemento a elemento ---
disp('Digite os 25 elementos da matriz 5x5:');
for i = 1:n
  for j = 1:n
    M(i, j) = input(sprintf('Elemento (%d,%d): ', i, j));
  end
end

% --- Monta a matriz resultante ---
% Diagonal principal -> elementos onde a linha e igual a coluna (i == j)
R = zeros(n, n);        % comeca toda com zeros
for i = 1:n
  for j = 1:n
    if i == j
      R(i, j) = 1;      % diagonal principal recebe 1
    end
  end
end

% --- Exibe os resultados ---
printf('\nMatriz original:\n');
disp(M);

printf('Matriz resultante (diagonal principal = 1, demais = 0):\n');
disp(R);
