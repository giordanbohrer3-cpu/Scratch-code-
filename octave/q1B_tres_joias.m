% =========================================================
% QUESTAO 1 - ALTERNATIVA B (Budismo - As Tres Joias)
% Solicita quantos budistas preferem BUDA, DHARMA e SANGHA.
% Informa o TOTAL e a MEDIA (com 2 casas decimais).
% =========================================================

buda   = input("Quantos budistas preferem BUDA? ");
dharma = input("Quantos budistas preferem DHARMA? ");
sangha = input("Quantos budistas preferem SANGHA? ");

total = buda + dharma + sangha;
media = total / 3;

printf("\nQuantidade TOTAL de budistas: %d\n", total);
printf("MEDIA das escolhas: %.2f\n", media);
