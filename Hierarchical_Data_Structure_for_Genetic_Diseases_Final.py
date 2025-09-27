# Hierarchical Data Structure for Genetic Diseases Using Tree Algorithms
# Asal Rabiee

import os

class Tree:
    def __init__(self):
        self.lst = []
        self.genes = {}
        self.gene_info = {}

    def get_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def Set_Sub_Disease(self, n):
        self.lst = []
        for i in range(n):
            data = input('Enter data of Subdisease: ')
            self.lst.append(data)
        self.write_to_file()

    def Set_Genes(self):
        self.genes = {}
        for disease in self.lst:
            k = self.get_int_input(f'Enter number of Genes for {disease}: ')
            self.genes[disease] = {}
            for i in range(k):
                gene_name = input(f'Enter name of Gene for {disease}: ')
                location = input(f'Enter location for {gene_name}: ')
                exon_count = input(f'Enter exon count for {gene_name}: ')
                official_full_name = input(f'Enter official full name for {gene_name}: ')
                gene_type = input(f'Enter gene type for {gene_name}: ')
                self.genes[disease][gene_name] = {
                    'location': location,
                    'exon': exon_count,
                    'official full name': official_full_name,
                    'gene type': gene_type
                }
        self.write_to_file()

    def Get_Sub_Disease(self):
        self.read_from_file()
        return self.lst

    def Get_Genes(self):
        self.read_from_file()
        return self.genes

    def write_to_file(self):
        os.makedirs('C:/Users/Asal/Desktop/data_structure', exist_ok=True)
        with open('C:/Users/Asal/Desktop/data_structure/DS-Project.txt', 'w') as myfile:
            myfile.write("Subdiseases:\n")
            for disease in self.lst:
                myfile.write(f"{disease}\n")
            myfile.write("\nGenes:\n")
            for disease, genes in self.genes.items():
                myfile.write(f"{disease}:\n")
                for gene_name, gene_info in genes.items():
                    gene_info_str = ', '.join([f"{key}: {value}" for key, value in gene_info.items()])
                    myfile.write(f"  {gene_name}: {gene_info_str}\n")


    def Search_Genome_of_Disease(self, subdisease):
        #read from file
        if subdisease in self.genes:
            print(f"Genes for {subdisease}:")
            for gene_name, gene_info in self.genes[subdisease].items():
                print(f"  Gene: {gene_name}")
                for key, value in gene_info.items():
                    print(f"    {key}: {value}")
        else:
            print(f"No genes found for subdisease: {subdisease}")

def menu():
    tree = Tree()
    while True:
        print('1 -> Create database')
        print('2 -> Searching genome of disease')
        print('3 -> Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            n = tree.get_int_input('Enter size of Subdisease: ')
            tree.Set_Sub_Disease(n)
            tree.Set_Genes()
        elif choice == '2':
            subdisease = input('Enter the subdisease to search genome: ')
            tree.Search_Genome_of_Disease(subdisease)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

menu()
