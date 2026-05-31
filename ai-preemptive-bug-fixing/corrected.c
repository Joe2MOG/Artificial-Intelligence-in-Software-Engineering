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
 * Return: pointer to the head of the list, or the same head if malloc fails
 *
 * Description:
 *   1. Allocates memory and immediately checks for failure.
 *   2. Initializes the new node fields right after allocation so
 *      no early return leaves garbage data.
 *   3. Traverses the list correctly, stopping at the LAST node,
 *      then links the new node through current->next.
 */
list_t *add_node_end(list_t *head, const int n)
{
	list_t *new_node, *current;

	new_node = malloc(sizeof(list_t));
	if (!new_node)          /* FIX: handle malloc failure */
		return (head);  /* return original list unchanged */
	new_node->n = n;
	new_node->next = NULL;  /* always initialize before any branch */

	if (!head)
		return (new_node);  /* empty list: new node becomes head */

	current = head;
	while (current->next)   /* FIX: stop at the last node, not past it */
		current = current->next;

	current->next = new_node;  /* FIX: actually link the node into the list */

	return (head);
}
