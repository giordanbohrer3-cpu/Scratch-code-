% =====================================================================
% Questao 6 - Programacao Algoritmica (Trabalho Octave - Matrizes)
% Le uma matriz 4x4 e encontra o elemento MINIMAX: o menor elemento da
% linha onde se encontra o MAIOR elemento da matriz. Mostra o valor do
% minimax e sua posicao (linha e coluna).
% =====================================================================

clc;
clear;

n = 4;                  % matriz 4x4
M = zeros(n, n);

% --- Leitura da matriz, elemento a elemento ---
disp('Digite os 16 elementos da matriz 4x4:');
for i = 1:n
  for j = 1:n
    M(i, j) = input(sprintf('Elemento (%d,%d): ', i, j));
  end
end

% --- 1) Localiza o MAIOR elemento da matriz inteira ---
maior = M(1, 1);
linha_maior = 1;
for i = 1:n
  for j = 1:n
    if M(i, j) > maior
      maior = M(i, j);
      linha_maior = i;     % guarda a linha onde esta o maior
    end
  end
end

% --- 2) Na linha do maior, encontra o MENOR elemento (o minimax) ---
minimax = M(linha_maior, 1);
col_minimax = 1;
for j = 1:n
  if M(linha_maior, j) < minimax
    minimax = M(linha_maior, j);
    col_minimax = j;       % guarda a coluna do menor dessa linha
  end
end

% --- Exibe os resultados ---
printf('\nMatriz informada:\n');
disp(M);

printf('Maior elemento da matriz: %g (esta na linha %d)\n', maior, linha_maior);
printf('Elemento minimax........: %g\n', minimax);
printf('Posicao do minimax......: linha %d, coluna %d\n', linha_maior, col_minimax);
