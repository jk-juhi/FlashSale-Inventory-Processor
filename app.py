from typing import List, Tuple, Optional


class Order:
    """
    Represents a single customer order.
    """

    def __init__(self, order_id: str, value: float):
        self.order_id = order_id
        self.value = value

    def __repr__(self):
        return f"({self.order_id}: ${self.value})"


class FineTunedFlashSale:
    """
    Flash Sale Inventory Order Processor

    Features:
    - In-place Insertion Sort (O(1) auxiliary space)
    - Two-Pointer Budget Pair Search (O(N))
    """

    def __init__(self):
        self.batch_orders: List[Order] = []

    def load_orders(self, orders: List[Order]):
        """
        Loads the incoming batch of orders.
        """
        self.batch_orders = orders

    def sort_orders_by_value_inplace(self):
        """
        Sorts orders by value using Insertion Sort.

        Time Complexity:
            O(N²)

        Auxiliary Space:
            O(1)
        """

        n = len(self.batch_orders)

        for i in range(1, n):

            current = self.batch_orders[i]

            j = i - 1

            while (
                j >= 0
                and self.batch_orders[j].value > current.value
            ):
                self.batch_orders[j + 1] = self.batch_orders[j]
                j -= 1

            self.batch_orders[j + 1] = current

    def find_budget_pair(
        self,
        target_budget: float
    ) -> Optional[Tuple[Order, Order]]:
        """
        Finds two orders whose combined value equals the target budget.

        Time Complexity:
            O(N)

        Auxiliary Space:
            O(1)
        """

        left = 0
        right = len(self.batch_orders) - 1

        while left < right:

            total = (
                self.batch_orders[left].value
                + self.batch_orders[right].value
            )

            if total == target_budget:
                return (
                    self.batch_orders[left],
                    self.batch_orders[right],
                )

            elif total < target_budget:
                left += 1

            else:
                right -= 1

        return None