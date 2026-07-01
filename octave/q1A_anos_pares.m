% =========================================================
% QUESTAO 1 - ALTERNATIVA A (Budismo)
% Lista na tela APENAS os anos PARES existentes entre os
% anos da vida de Buda: -566 AEC (nascimento) e -483 AEC
% (falecimento).
% =========================================================

printf("Anos PARES entre -566 e -483:\n");

for ano = -566:-483
  if mod(ano, 2) == 0
    printf("%d\n", ano);
  end
end
