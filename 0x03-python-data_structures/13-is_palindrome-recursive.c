#include "lists.h"

/**
 * is_palindrome - wrapper function for check_palindrome
 *
 * @head: head node of list
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
	{
		return (0);
	}
	return (check_palindrome(head, (*head)));
}

/**
 * check_palindrome - checks whether a linked list is a palindrome by recursion
 *
 * @left: left node
 * @right: right node
 *
 * Return: 1 if palindrome, 0 if not
 */
int check_palindrome(listint_t **left, listint_t *right)
{
	int is_palindrome;

	/* stop recursion when right becomes null */
	if (right == NULL)
	{
		return (1);
	}

	is_palindrome = check_palindrome(left, right->next);
	if (is_palindrome == 0)
	{
		return (0);
	}

	int is_palindrome2 = ((*left)->n == right->n);
	/* move to next node */
	*left = (*left)->next;

	return (is_palindrome2);
}
