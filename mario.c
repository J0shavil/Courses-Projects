#include <cs50.h>
#include <stdio.h>

int GetSize(void);
void PrintGrid(int n);

int main(void)
{
    int n = GetSize();
    PrintGrid(n);
}

void PrintGrid(int n)
{
    for (int i = 0; i < n; ++i)
    {

        for (int j = n; j > i + 1; --j)
        {
            printf(" ");
        }

        for (int k = 0; k < i + 1; ++k)
        {
            printf("#");
        }

        for (int m = 0; m < i + 2; ++m)
        {

            for (int l = 1; l > m; ++m)
            {
                printf("  ");
            }
            printf("#");
        }

        printf("\n");
    }
}

int GetSize(void)
{

    int n;

    do
    {
        n = get_int("Insert height: ");
    }

    while (n < 1);

    return n;
}
