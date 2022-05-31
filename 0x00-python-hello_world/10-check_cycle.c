#include "lists.h"

/**
 * check_cycle - checks whether a list has cycles
 *
 * @list: the list to check
 *
 * Description: uses Floyd’s Cycle-Finding Algorithm
 * -------------------------------
 * A hash table can also be used:
 * Traverse the given linked list and put the address of each node in a Hash table.
 * If you reach a node whose next pointer is NULL, then given linked list doesn't
 * contain s cycle.
 * If address of any node already exist in Hash table, it means we are visiting this node
 * again and linked list contains a cycle.
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
