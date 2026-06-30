%Lista Matrizes - Ex. 03: Elabore um algoritmo que leia uma matriz A 7x7, de
%numeros inteiros. Crie 2 vetores, VL(7) e VC(7), que contenham,
%respectivamente, o primeiro elemento de todas as linhas e o ultimo elemento
%de todas as colunas. Mostre a matriz e os vetores resultantes.

%Le a Matriz A(7,7)
disp('Matriz A');
for I=1:7 %Linhas
  fprintf('\nLinha %d ',I);
  for J=1:7 %Colunas
     fprintf('\nColuna %d:',J);
     A(I,J)=input(' ');
  end
end

%VL = primeiro elemento de cada linha (coluna 1)
for I=1:7
  VL(I)=A(I,1);
end

%VC = ultimo elemento de cada coluna (ultima linha, linha 7)
for J=1:7
  VC(J)=A(7,J);
end

%Mostra a matriz digitada
disp('Matriz A Digitada');
for I=1:7 %Linhas
   fprintf('\n');
   for J=1:7 %Colunas
     fprintf('\t%d',A(I,J));
   end
end

%Mostra o vetor VL (primeiro elemento de cada linha)
fprintf('\n\nVetor VL (primeiro elemento de cada linha):\n');
for I=1:7
  fprintf('\t%d',VL(I));
end

%Mostra o vetor VC (ultimo elemento de cada coluna)
fprintf('\n\nVetor VC (ultimo elemento de cada coluna):\n');
for J=1:7
  fprintf('\t%d',VC(J));
end
fprintf('\n');
