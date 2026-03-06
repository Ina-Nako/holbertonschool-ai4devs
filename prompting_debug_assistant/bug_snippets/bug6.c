#include <stdio.h>
#include <string.h>

/**
 * reverse_string - Reverses a string in place.
 * @str: The string to reverse.
 */
void reverse_string(char *str)
{
    int len = strlen(str);
    int i;

    for (i = 0; i <= len / 2; i++)
    {
        char temp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = temp;
    }
}

int main(void)
{
    char s1[] = "hello";
    char s2[] = "abcd";
    char s3[] = "a";

    reverse_string(s1);
    printf("%s\n", s1);  /* Expected: olleh */

    reverse_string(s2);
    printf("%s\n", s2);  /* Expected: dcba */

    reverse_string(s3);
    printf("%s\n", s3);  /* Expected: a */

    return 0;
}
