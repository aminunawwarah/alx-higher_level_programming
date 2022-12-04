#include "lists.h"

/**
 * reverse - reverses the other half
 *
 * @h_r: beginning of the second half
 * Return: returns nothing
 */
void reverse(listint_t **h_r)
{
    listint_t *prv;
    listint_t *crr;
    listint_t *nxt;

    prv = NULL;
    crr = *h_r;

    while (crr != NULL)
    {
        nxt = crr->next;
        crr->next = prv;
        prv = crr;
        crr = nxt;
    }

    *h_r = prv;
}

/**
 * compare - compares individual integers
 *
 * @h1: beginning of the first part
 * @h2: beginning of the middle part
 * Return: returns 1 if they are equal otherwise 0
 */
int compare(listint_t *h1, listint_t *h2)
{
    listint_t *tmp1;
    listint_t *tmp2;

    tmp1 = h1;
    tmp2 = h2;

    while (tmp1 != NULL && tmp2 != NULL)
    {
        if (tmp1->n == tmp2->n)
        {
            tmp1 = tmp1->next;
            tmp2 = tmp2->next;
        }
        else
        {
            return (0);
        }
    }

    if (tmp1 == NULL && tmp2 == NULL)
    {
        return (1);
    }

    return (0);
}

/**
 * is_palindrome - finds whether a singly linked list
 * is a palindrome
 * @head: pointer to the beginning of the list
 * Return: returns 0 if it is not a palindrome,
 * otherwise 1
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev_slow;
    listint_t *scn_half, *middle;
    int isp;

    slow = fast = prev_slow = *head;
    middle = NULL;
    isp = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            prev_slow = slow;
            slow = slow->next;
        }

        if (fast != NULL)
        {
            middle = slow;
            slow = slow->next;
        }

        scn_half = slow;
        prev_slow->next = NULL;
        reverse(&scn_half);
        isp = compare(*head, scn_half);

        if (middle != NULL)
        {
            prev_slow->next = middle;
            middle->next = scn_half;
        }
        else
        {
            prev_slow->next = scn_half;
        }
    }

    return (isp);
}
