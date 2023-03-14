#include "lists.h"

int *arr_int(listint_t **head, int *i);

/**
*is_palindrome - function in C that checks if a singly
*linked list is a palindrome
*@head: start of the list
*Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *start, *end, *ptr;
	int i, j, k;

	if (*head == NULL)
		return (1);

	ptr = *head;
	i = 0;
	while (ptr != NULL)
	{
		i++;
		ptr = ptr->next;
	}

	start = *head;
	j = i / 2;

	while (start != NULL && j >= 0)
	{
		end = *head;
		k = 0;
		while (end != NULL && k < i - 1)
		{
			k++;
			end = end->next;
		}
		if (start->n != end->n)
			return (0);

		start = start->next;
		j--;
		i--;
	}

	return (1);
}
