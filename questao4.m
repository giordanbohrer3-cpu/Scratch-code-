% =====================================================================
% Questao 4 - Programacao Algoritmica (Trabalho Octave - Matrizes)
% Le uma matriz 4x3 (4 linhas, 3 colunas). No final apresenta o numero
% de elementos PARES e o numero de IMPARES, mostrando tambem o percentual
% em relacao ao total de elementos.
% =====================================================================

clc;
clear;

linhas = 4;
colunas = 3;
M = zeros(linhas, colunas);

% --- Leitura da matriz, elemento a elemento ---
disp('Digite os 12 elementos da matriz 4x3:');
for i = 1:linhas
  for j = 1:colunas
    M(i, j) = input(sprintf('Elemento (%d,%d): ', i, j));
  end
end

% --- Conta pares e impares ---
pares = 0;
impares = 0;
for i = 1:linhas
  for j = 1:colunas
    if mod(M(i, j), 2) == 0
      pares = pares + 1;        % divisivel por 2 -> par
    else
      impares = impares + 1;    % caso contrario -> impar
    end
  end
end

total = linhas * colunas;       % total de elementos (12)
perc_pares = (pares / total) * 100;
perc_impares = (impares / total) * 100;

% --- Exibe os resultados ---
printf('\nMatriz informada:\n');
disp(M);

printf('Quantidade de elementos PARES...: %d (%.2f%%)\n', pares, perc_pares);
printf('Quantidade de elementos IMPARES.: %d (%.2f%%)\n', impares, perc_impares);
