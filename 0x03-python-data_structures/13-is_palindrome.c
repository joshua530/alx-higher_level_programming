#include "lists.h"

/**
 * is_palindrome - checks whether a linked list is a palindrome
 *
 * @head: linked list's head node
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy_head = NULL, *current, *tmp;

	if (*head == NULL)
	{
		return (1);
	}

	current = *head;
	/* copy original linked list in reverse order */
	copy_head = copy_reverse(*head);
	if (copy_head == NULL)
	{
		return (0);
	}

	/* compare the two lists node by node */
	current = *head;
	tmp = copy_head; /* reversed list iterator */
	while (current && tmp)
	{
		if (current->n != tmp->n)
		{
			return (0);
		}
		current = current->next;
		tmp = tmp->next;
	}

	if (tmp == NULL)
	{
		free_listint(copy_head);
	}

	return (1);
}

/**
 * copy_reverse - copies a list in reverse order
 *
 * @head: head node of list to be copied
 *
 * Return: head node of copied list or NULL if copying failed
 */
listint_t *copy_reverse(listint_t *head)
{
	listint_t *copy_head, *tmp, *current;

	current = head;
	/* copy original linked list in reverse order */
	while (current)
	{
		if (copy_head == NULL)
		{
			copy_head = create_node(current->n, NULL);
			if (copy_head == NULL)
			{
				return (NULL);
			}
		}
		else
		{
			tmp = create_node(current->n, NULL);
			if (tmp == NULL)
			{
				free_listint(copy_head);
				return (NULL);
			}
			tmp->next = copy_head;
			copy_head = tmp;
		}
		current = current->next;
	}

	return (copy_head);
}

/**
 * create_node - instantiates a new node
 *
 * @n: the node's value
 * @next: the next node
 *
 * Return: created node or NULL if node creation failed
 */
listint_t *create_node(int n, listint_t *next)
{
	listint_t *node = malloc(sizeof(listint_t));

	if (node == NULL)
	{
		return (NULL);
	}
	node->n = n;
	node->next = next;
	return (node);
}
