#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts node in a sorted linked list
 *
 * @head: head node
 * @number: number to insert
 *
 * Return: address of newly created node or NULL if node creation
 * failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new, *prev;

	/* head node */
	if (number <= current->n)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
		{
			return (NULL);
		}
		new->n = number;
		new->next = current;
		current = new;
		return (new);
	}

	prev = current;
	current = prev->next;
	while (current != NULL)
	{
		if (number <= current->n)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
			{
				return (NULL);
			}
			new->n = number;
			new->next = current;
			prev->next = new;
			return (new);
		}
		prev = current;
		current = current->next;
	}

	return (NULL);
}
