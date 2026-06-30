%Lista Matrizes - Ex. 02: Crie um programa que leia uma matriz M(4,4) e um
%valor A. Multiplique a matriz M pelo valor A armazenando o resultado em um
%vetor V(16). Mostre o vetor V.

%Le o valor A
A=input('Digite o valor A: ');

%Le a Matriz M(4,4)
disp('Matriz M');
for I=1:4 %Linhas
  fprintf('\nLinha %d ',I);
  for J=1:4 %Colunas
     fprintf('\nColuna %d:',J);
     M(I,J)=input(' ');
  end
end

%Multiplica M por A guardando o resultado no vetor V(16)
K=1; %Indice do vetor
for I=1:4
  for J=1:4
    V(K)=M(I,J)*A;
    K++;
  end
end

%Mostra o vetor V
fprintf('\nVetor V (M * %d):\n',A);
for K=1:16
  fprintf('\t%d',V(K));
end
fprintf('\n');
