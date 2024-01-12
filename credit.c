#include <cs50.h>
#include <stdio.h>
#include <string.h>

int count = 15;
long creditNum;
int creditcard[16];
int calculate[8];
int calculateRest[8];
int count2 = 0;
int n = 0;
int n2 = 0;
int calculateCount = 0;
int calculateRestCount = 0;
bool validCard = true;
bool AMEX = false;
bool MASTERCARD = false;
bool VISA = false;
bool AMEXLENGTH = false;
bool VISALENGTH = false;
bool MCLENGTH = false;

int main(void)
{
    creditNum = get_long("Number: ");

    do
    {
        // printf("COUNT TOP: %i\n", count);
        // printf("COUNT2: %i\n", count2);
        // printf("CreditNUM MOD: %ld\n", creditNum % 10);
        // printf("CreditNUM: %ld\n", creditNum);
        // printf("N VALUE: %i\n", n);
        if (count % 2 > 0)
        {

            calculateRest[n2] = creditNum % 10;
            n2++;
        }

        creditcard[count] = creditNum % 10;

        if (count % 2 == 0)
        {
            n++;
            calculate[n] = creditNum % 10;
        }

        count--;
        creditNum /= 10;
    }
    while (creditNum != 0);

    for (int i = 0; i < 16; ++i)
    {
        if (creditcard[0] == 5 && creditcard[1] <= 5 && creditcard[1] != 0)
        {
            MCLENGTH = true;
        }
        if (i == 1 && creditcard[i] == 3 && creditcard[i + 1] == 4)
        {
            AMEXLENGTH = true;
        }
        if (i == 1 && creditcard[i] == 3 && creditcard[i + 1] == 7)
        {
            AMEXLENGTH = true;
        }
        if (i == 3 && creditcard[i] == 4)
        {
            VISALENGTH = true;
        }
        if (creditcard[0] == 4)
        {
            VISALENGTH = true;
            // printf("Visa lenght true\n");
        }
    }

    for (int i = 8; i >= 0; --i)
    {
        // printf("%i", calculate[i]);
        calculate[i] = calculate[i] * 2;
    }

    // printf("\n");

    for (int i = 8; i >= 0; --i)
    {
        // printf("%i", calculate[i]);
        if (calculate[i] > 9)
        {
            calculateCount += calculate[i] % 10;
            calculateCount += calculate[i] / 10;
        }
        else
        {
            calculateCount += calculate[i];
        }
    }

    // printf("\n");

    // printf("Calulate rest: ");

    for (int i = 0; i < 8; ++i)
    {
        // printf("%i", calculateRest[i]);
        calculateRestCount += calculateRest[i];
    }
    // printf("\n");
    calculateCount += calculateRestCount;

    /// printf("Calculate Count: %i\n", calculateCount);

    // printf("CalculateCount Mod : %i\n", calculateCount % 10);

    if (VISALENGTH == true && calculateCount % 10 != 0)
    {

        printf("INVALID\n");
    }

    if (VISALENGTH == true && calculateCount % 10 == 0)
    {
        printf("VISA\n");
    }
    if (AMEXLENGTH == true && calculateCount % 10 == 0)
    {
        printf("AMEX\n");
    }
    else if (AMEXLENGTH != true && calculateCount % 10 < 0)
    {
        printf("INVALID\n");
    }

    if (MCLENGTH == true)
    {
        printf("MASTERCARD\n");
    }
    else if (MCLENGTH != true && calculateCount % 10 < 0)
    {
        printf("INVALID\n");
    }

    // printf("\n");

    if (VISALENGTH != true && MCLENGTH != true && AMEXLENGTH != true)
    {
        printf("INVALID\n");
    }
