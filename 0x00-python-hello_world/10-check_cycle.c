#include "lists.h"
/**
 *check_cycle - function in C that checks
 *if a singly linked list has a cycle in it
 *@list: pointer to a singly-linked list
 *Return: 1 for yes otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *ahead, *behind;

	if (list != NULL)
	{
		behind = list;
		ahead = (*list).next;

		while (ahead != NULL && (*ahead).next != NULL)
		{
			if (ahead == behind)
				return (1);

			ahead = (*ahead).next->next;
			behind = (*behind).next;
		}

		return (0);
	}

	return (0);
}
