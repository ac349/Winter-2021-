mol = Chem.MolFromSmiles("C[N+](CC1=CC=C(C[C@H](CN/C(N)=[N+]([H])\[H])[C@H]2NC(C(NC3=CC=C(Cl)C(F)=C3)=O)=O)C2=C1)([H])CC")

patt=Chem.MolFromSmiles("C12=CC=CC=C1CCC2")
r=mol.GetSubstructMatch(patt)
bis = mol.GetSubstructMatches(Chem.MolFromSmarts('[!R][R]'))
bs = [mol.GetBondBetweenAtoms(x,y).GetIdx() for x,y in bis if y in r]
gs=[y for x,y in bis if y in r]
nb=Chem.FragmentOnBonds(mol,bs)
h=Chem.MolToSmiles(nb)
pq=h.split(".")
jl={i:i.split('*]')[0].split('[')[1] for i in pq if int(i.split('*]')[0].split('[')[1]) in gs}
pprint.pprint(jl)
indane_smi='C12=CC=CC=C1CCC2'
indane_mol=Chem.MolFromSmiles(indane_smi) 
mol = Chem.MolFromSmiles("C[N+](CC1=CC=C(C[C@H](CN/C(N)=[N+]([H])\[H])[C@H]2NC(C(NC3=CC=C(Cl)C(F)=C3)=O)=O)C2=C1)([H])CC")
bis = mol.GetSubstructMatches(Chem.MolFromSmiles(indane_smi))
smi_atoms = np.array(bis[0])
smi2str = [-1,4,5,6,7,-1,1,2,3] 
>>>>>>>>>>
   {'[15*]NC(=O)C(=O)Nc1ccc(Cl)c(F)c1': '15',
    '[3*]C[NH+](C)CC': '3',
    '[8*]CN/C(N)=[NH+]\\[H]': '8'}
 indane_smi='C12=CC=CC=C1CCC2'
indane_mol=Chem.MolFromSmiles(indane_smi) 
mol = Chem.MolFromSmiles("C[N+](CC1=CC=C(C[C@H](CN/C(N)=[N+]([H])\[H])[C@H]2NC(C(NC3=CC=C(Cl)C(F)=C3)=O)=O)C2=C1)([H])CC")
bis = mol.GetSubstructMatches(Chem.MolFromSmiles(indane_smi))
smi_atoms = np.array(bis[0])
smi2str = [-1,4,5,6,7,-1,1,2,3] 
map_dict={k: v for k,v in zip(smi_atoms,smi2str)}
print(map_dict)
>>>>>>>>
{6: -1, 5: 4, 4: 5, 3: 6, 31: 7, 30: -1, 15: 1, 8: 2, 7: 3}
