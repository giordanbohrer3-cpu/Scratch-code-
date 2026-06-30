% =====================================================================
% Questao 3 - Programacao Algoritmica (Trabalho Octave - Matrizes)
% Le uma matriz 6x6 e calcula a SOMA dos elementos da diagonal secundaria.
% =====================================================================

clc;
clear;

n = 6;                  % matriz 6x6
M = zeros(n, n);

% --- Leitura da matriz, elemento a elemento ---
disp('Digite os 36 elementos da matriz 6x6:');
for i = 1:n
  for j = 1:n
    M(i, j) = input(sprintf('Elemento (%d,%d): ', i, j));
  end
end

% --- Soma da diagonal secundaria (i + j = n + 1 = 7) ---
soma = 0;
for i = 1:n
  for j = 1:n
    if (i + j) == (n + 1)
      soma = soma + M(i, j);
    end
  end
end

% --- Exibe os resultados ---
printf('\nMatriz informada:\n');
disp(M);

printf('Soma dos elementos da diagonal secundaria: %g\n', soma);
