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
	listint_t *start;
	int i, j, *end;

	if (*head == NULL)
		return (1);

	i = 0;
	end = arr_int(head, &i);
	start = *head;
	j = i / 2;

	while (start != NULL && i >= j)
	{
		if (start->n != end[i])
			return (0);

		start = start->next;
		i--;
	}

	free(end);
	return (1);
}

/**
*@arr_int - function to generate an array of ints
*@head: pointer to list
*@i: pointer to size of an array generated
*Return: an array of ints
*/

int *arr_int(listint_t **head, int *i)
{
	listint_t *ptr = *head;
	int *arr;
	int j = 0;

	while (ptr)
	{
		i++;
		j++;
		ptr = ptr->next;
	}

	arr = malloc(sizeof(int) * j);

	if (arr == NULL)
		return (NULL);
	ptr = *head;
	j = 0;

	while (ptr)
	{
		arr[j] = ptr->n;
		j++;
		ptr = ptr->next;
	}

	return (arr);
}
