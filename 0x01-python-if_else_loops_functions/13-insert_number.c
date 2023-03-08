#include "lists.h"

/**
 * insert_node - inserts a number into a sorted list
 * @head: pointer to the list
 * @number: number to add
 * Return: address of the added node else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new, *temp;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	temp = NULL;
	ptr = *head;

	while (ptr != NULL && ptr->n < number)
	{
		temp = ptr;
		ptr = ptr->next;
	}

	new->next = ptr;

	if (temp != NULL)
		temp->next = new;
	else
		*head = new;

	return (new);
}
