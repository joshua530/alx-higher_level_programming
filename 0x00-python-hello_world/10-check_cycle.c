#include "lists.h"

/**
 * check_cycle - checks whether a list has cycles
 *
 * @list: the list to check
 *
 * Description: uses Floyd’s Cycle-Finding Algorithm
 *
 * Return: 0 if no cycle; 1 if  cycle exists
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;
	listint_t *head = tmp = list;

	while (head && tmp && tmp->next)
	{
		head = head->next;
		tmp = tmp->next->next;
		if (head == tmp) /* back to where we started */
		{
			return (1);
		}
	}

	return (0);
}
