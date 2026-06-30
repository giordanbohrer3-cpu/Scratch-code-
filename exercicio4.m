%Lista Matrizes - Ex. 04: Escreva um programa que leia uma matriz A
%de duas dimensoes, com 5 linhas e 3 colunas, contendo numeros inteiros.
%No final, apresente o total de elementos PARES e o total de IMPARES.

%Inicializa totais
Pares=0;
Impares=0;

%Le Matriz
disp('Matriz A');
for I=1:5 %Linhas
  fprintf('\nLinha %d ',I);
  for J=1:3 %Colunas
     fprintf('\nColuna %d:',J);
     MatA(I,J)=input(' ');
  end
end
%Mostra Matriz
disp('Matriz A Digitada');
for I=1:5 %Linhas
   fprintf('\n');
   for J=1:3 %Colunas
     fprintf('\t%d',MatA(I,J));
   end
end

%Verifica se e par ou impar
for I=1:5
  for J=1:3
    if mod(MatA(I,J),2) == 0  %Testa PAR
      Pares++;
    else
      Impares++;
    end
  end
end

%Mostra resposta
fprintf('\nDigitados %d Pares e %d Impares\n',Pares,Impares);
