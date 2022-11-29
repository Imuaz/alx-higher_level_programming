#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list has a cycle.
 * @list:the singly-linked list to check7.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *dest;

	if (list == NULL || list->next == NULL)
		return (0);

	current = list->next;
	dest = list->next->next;

	while (current && dest  && dest->next)
	{
		if (current == dest)
			return (1);

		current = current->next;
		dest = dest->next->next;
	}

	return (0);
}
