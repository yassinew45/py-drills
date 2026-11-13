import pytest
from oop.account import Account, SavingsAccount

# test_cannot_instantiate_abstract_account: Account("Ali") should raise TypeError. Use with pytest.raises(TypeError).
def test_cannot_instantiate_abstract_account():
    with pytest.raises(TypeError):     # passes only if the block inside raises TypeError
        Account("Ali")                 # no need to store the result in a variable

# test_savings_withdraw_too_much: withdrawing more than the balance should raise ValueError
def test_savings_withdraw_too_much():
    account = SavingsAccount("Ali", 0.05, 50)
    with pytest.raises(ValueError, match="balance"):
        account.withdraw(100)  ## ValueError: amount must be positive and less than the balance

# test_equality_and_repr: two SavingsAccounts with the same owner and balance are equal, and repr(account) contains the class name.
def test_equality_and_repr():
    account1 = SavingsAccount("Ali", 0.05)
    account2 = SavingsAccount("Ali", 0.05)
    account3 = SavingsAccount("Yassine", 0.05)
    account4 = SavingsAccount("Yassine", 0.05)

    assert account1 == account2
    assert account1 != account3
    assert account3 == account4

    account4.deposit(5000)
    assert account3 != account4
    assert "Ali" in repr(account1)
    assert "Ali" not in repr(account3)
    assert "SavingsAccount" in repr(account1)

    # test that an account is not equal to a non-account object
    assert account1 != "Ali"
    assert account1 != 10
    assert account1 is not None


def test_deposit_increases_balance():
    account = SavingsAccount("Ali", 0.05, 50)

    account.deposit(25)

    assert account.balance == 75


@pytest.mark.parametrize("amount", [0, -1])
def test_deposit_rejects_non_positive_amount(amount):
    account = SavingsAccount("Ali", 0.05, 50)

    with pytest.raises(ValueError, match="positive"):
        account.deposit(amount)

    assert account.balance == 50


def test_withdraw_allows_withdrawing_the_full_balance():
    account = SavingsAccount("Ali", 0.05, 50)

    account.withdraw(50)

    assert account.balance == 0


@pytest.mark.parametrize("amount", [0, -1])
def test_withdraw_rejects_non_positive_amount(amount):
    account = SavingsAccount("Ali", 0.05, 50)

    with pytest.raises(ValueError, match="positive"):
        account.withdraw(amount)

    assert account.balance == 50


def test_add_interest_increases_balance():
    account = SavingsAccount("Ali", 0.05, 100)

    account.add_interest()

    assert account.balance == pytest.approx(105)