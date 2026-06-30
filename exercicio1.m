%Lista Matrizes - Ex. 01: Crie um programa que leia uma matriz M(6,6) e um
%valor A. Multiplique a matriz M pelo valor A. Mostre a matriz resultante.

%Le o valor A
A=input('Digite o valor A: ');

%Le a Matriz M(6,6)
disp('Matriz M');
for I=1:6 %Linhas
  fprintf('\nLinha %d ',I);
  for J=1:6 %Colunas
     fprintf('\nColuna %d:',J);
     M(I,J)=input(' ');
  end
end

%Multiplica cada elemento de M pelo valor A
for I=1:6
  for J=1:6
    R(I,J)=M(I,J)*A;
  end
end

%Mostra a matriz resultante
fprintf('\nMatriz Resultante (M * %d):\n',A);
for I=1:6 %Linhas
   fprintf('\n');
   for J=1:6 %Colunas
     fprintf('\t%d',R(I,J));
   end
end
fprintf('\n');
