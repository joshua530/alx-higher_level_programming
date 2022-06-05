#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);
listint_t *create_node(int n, listint_t *next);
listint_t *copy_reverse(listint_t *head);
int check_palindrome(listint_t **right, listint_t *left);

#endif /* LISTS_H */
