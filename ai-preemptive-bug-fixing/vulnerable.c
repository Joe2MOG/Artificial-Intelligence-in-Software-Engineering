#include <stdlib.h>

/**
 * struct list_s - singly linked list
 * @n: integer stored in the node
 * @next: pointer to the next node
 */
typedef struct list_s
{
	int n;
	struct list_s *next;
} list_t;

/**
 * add_node_end - adds a new node at the end of a list_t list
 * @head: pointer to the head of the list
 * @n: integer to store in the new node
 *
 * Return: pointer to the head of the list
 *
 * Note: This version contains intentional flaws for review.
 */
list_t *add_node_end(list_t *head, const int n)
{
	list_t *new_node = malloc(sizeof(list_t));
	list_t *current = head;

	if (!head)
		return (new_node);
	while (current)
		current = current->next;
	current = new_node;
	new_node->n = n;
	new_node->next = NULL;
	return (head);
}
