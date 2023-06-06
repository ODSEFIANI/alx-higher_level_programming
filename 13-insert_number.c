#include "lists.h"

/**
 * insert_node - Inserts a Num Into A Sorted Singly-Linked List.
 * @head: A Pointer the Head of The linked list.
 * @number: The Num To Insert.
 *
 * Return: If The Function fails - NULL.
 *         Otherwise - a Pointer To The New Node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
