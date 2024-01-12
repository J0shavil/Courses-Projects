#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

string input;

int count_letters(string text);
int count_words(string words);
int count_sentences(string sentences);
int size;
int word_number = 0;
int letter_count = 0;
int sentence_count = 0;
float L;
float S;
float index;

int main(void)
{
    input = get_string("Text: ");
    count_letters(input);
    count_words(input);
    count_sentences(input);
    L = (float) letter_count / (float) word_number * 100;
    S = (float) sentence_count / (float) word_number * 100;
    index = 0.0588 * L - 0.296 * S - 15.8;

    // printf("index: %f\n", index);

    if (index > 16)
    {
        printf("Grade 16+\n");
    }
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index < 16)
    {
        printf("Grade %i\n", (int) round(index));
    }
}

int count_letters(string text)
{
    size = strlen(text);
    for (int i = 0; i < size; ++i)
    {
        if (input[i] > 64 & input[i] < 91 || input[i] > 96 & input[i] < 123)
        {
            letter_count++;
        }
    }

    // printf("%i letters\n", letter_count);
    return letter_count;
}

int count_words(string words)
{

    for (int i = 0; i < size; ++i)
    {
        // if(input[i+1] == ' ' & input[i] != '.' || input[i+1] == ',' || input[i+1] == '.' || input[i+1] == ' ' & input[i] != '!' )
        if (input[i + 1] == '.' & input[i + 2] != ' ' || input[i + 1] == '!' || input[i + 1] == '?' ||input[i] != ',' & input[i + 1] == ' ' || input[i + 1] == ',')
        {
            word_number++;
        }
    }
    // printf("%i words\n", word_number);

    return word_number;
}

int count_sentences(string sentences)
{

    for (int i = 0; i < size; ++i)
    {
        if (input[i] == '.' & input[i + 1] != ' ' || input[i] == '.' & input[i + 1] == ' ' || input[i] == '!' & input[i + 1] != ' ' || input[i] == '!' & input[i + 1] == ' ' || input[i] == '?' & input[i + 1] != ' ' || input[i] == '?' & input[i + 1] == ' ' )
        {
            sentence_count++;
        }
    }
    // printf("%i sentences\n", sentence_count);
    return sentence_count;
}