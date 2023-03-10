#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *start, *end, *ptr;
	int i, j , k;

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
	j = i / 2 ;

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
