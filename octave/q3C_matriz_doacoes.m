% =========================================================
% QUESTAO 3 - ALTERNATIVA C (Catolicismo)
% Solicita os valores de doacoes realizados por fieis durante
% um mes e armazena em uma matriz 5x6. Mostra a matriz.
% Informa quantas doacoes PARES e quantas IMPARES existem na
% matriz e escreve o PERCENTUAL (2 casas decimais) de pares
% e impares em relacao a quantidade total de doacoes.
% =========================================================

M = zeros(5, 6);

% Leitura da matriz 5x6
for i = 1:5
  for j = 1:6
    M(i, j) = input(sprintf("Valor da doacao [linha %d, coluna %d]: ", i, j));
  end
end

printf("\nMatriz 5x6 de doacoes:\n");
disp(M);

% Contagem de doacoes pares e impares
pares   = 0;
impares = 0;
for i = 1:5
  for j = 1:6
    if mod(M(i, j), 2) == 0
      pares = pares + 1;
    else
      impares = impares + 1;
    end
  end
end

total = 5 * 6;   % 30 doacoes no total

printf("\nQuantidade de doacoes PARES: %d\n", pares);
printf("Quantidade de doacoes IMPARES: %d\n", impares);
printf("Percentual de PARES: %.2f%%\n", (pares / total) * 100);
printf("Percentual de IMPARES: %.2f%%\n", (impares / total) * 100);
