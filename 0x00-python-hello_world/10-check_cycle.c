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
	listint_t *head = list;

	while (head != NULL)
	{
		tmp = head->next;
		while (tmp != NULL)
		{
			if (head == tmp) /* back to where we started */
			{
				return (1);
			}
			tmp = tmp->next;
		}
		head = head->next;
	}

	return (0);
}
