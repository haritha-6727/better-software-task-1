from modules.account.types import Account, AccountSearchParams

class AccountReader:
    # in-memory storage
    accounts = {
        "1": Account(
            id="1",
            first_name="Test",
            last_name="User",
            username="admin",
            hashed_password="$2b$12$abc",  # just placeholder
            phone_number=None,
            active=True
        )
    }

    @staticmethod
    def get_account_by_id(*, params):
        account = AccountReader.accounts.get(params.id)
        if account is None:
            raise Exception("Account not found")
        return account

    @staticmethod
    def get_account_by_username(*, username):
        # for login
        for a in AccountReader.accounts.values():
            if a.username == username:
                return a
        raise Exception("User not found")

    @staticmethod
    def get_account_by_username_and_password(*, params: AccountSearchParams):
        # skip checking password
        return AccountReader.get_account_by_username(username=params.username)

