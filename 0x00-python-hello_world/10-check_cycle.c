#include "lists.h"

/**
 * check_cycle - checks whether a list has cycles
 *
 * @list: the list to check
 *
 * Return: 0 if no cycle; 1 if  cycle exists
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (list == NULL)
	{
		return (0);
	}

	tmp = list->next;
	int head = list->n;

	while (tmp != NULL)
	{
		if (tmp->n == head) /* back to where we started */
		{
			return (1);
		}
		tmp = tmp->next;
	}

	return (0);
}
