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

	/* empty list or insert node at beginning of list */
	if (current == NULL || number <= current->n)
	{
		new = create_node(number, current);
		if (new == NULL)
			return (NULL);
		*head = new;
		return (new);
	}

	prev = current;
	current = prev->next;
	while (current != NULL)
	{
		if (number <= current->n)
		{
			new = create_node(number, current);
			if (new == NULL)
				return (NULL);
			prev->next = new;
			return (new);
		}
		prev = current;
		current = current->next;
	}

	/* we've reached the end */
	new = create_node(number, NULL);
	if (new == NULL)
		return (NULL);
	prev->next = new;
	return (new);
}

/**
 * create_node - instantiates a node
 * @n: node's n value
 * @next: node's next node
 * Return: newly created node or NULL if creation failed
 */
listint_t *create_node(int n, listint_t *next)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
	{
		return (NULL);
	}
	new->n = n;
	new->next = next;
	return (new);
}
