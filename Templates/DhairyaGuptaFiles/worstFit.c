#include<stdio.h>
#define max 25
void main()
{
	int frag[max], b[max], f[max], i, j, nb, nf, temp;
	static int bf[max], ff[max];
	printf("\nEnter the number of blocks: ");
	scanf("%d", &nb);
	printf("Enter the number of process: ");
	scanf("%d", &nf);
	printf("\nEnter the size of the blocks:\n");
	for (i = 1; i <= nb; i++){
		printf("Block %d: ", i);
		scanf("%d", &b[i]);
	}
	printf("Enter the size of the process:\n");
	for (i = 1; i <= nf; i++){
		printf("File %d: ", i);
		scanf("%d", &f[i]);
	}
	for (i = 1; i <= nf; i++){
		temp = -1;
		for (j = 1; j <= nb; j++)
		{
			if (bf[j] != 1 && b[j] >= f[i])
			{
				temp = j;
				break;
			}
		}
		if (temp != -1)
		{
			ff[i] = temp;
			bf[temp] = 1;
			frag[i] = b[temp] - f[i];
		}
		else 
		{
			frag[i] = -1;
		}
	}
	printf("\nprocess_no:\tprocess_size :\tBlock_no: \tBlock_size: \tFragment\n");
	for (i = 1; i <= nf; i++)
	{
		printf("%d\t\t%d\t\t", i, f[i]);
		if (frag[i] != -1)
		{
			printf("%d\t\t%d\t\t%d\n", ff[i], b[ff[i]], frag[i]);
		}
		else
		{
			printf("Not Allocated\n");
		}
	}
}
