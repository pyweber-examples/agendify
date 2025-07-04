from manage_sql import SQLITE

class Database:
    def __init__(self):
        self.db = SQLITE(database='tasks')
        self.tablename = 'tasks'
        self.columns = ['title', 'description', 'datetime', 'email', 'status']
        self.create_table()
    
    def create_table(self):
        self.db.create_table(
            tablename=self.tablename,
            columns=[
                self.db.Column(
                    name=column,
                    column_type=self.db.Column_types.text
                ) for column in self.columns
            ]
        )
    
    def insert_task(self, title: str, description: str, datetime: str, email: str, status: str):
        try:
            self.db.insert_data(
                tablename=self.tablename,
                insert_query=[
                    self.db.ColumnData(
                        column=column,
                        value=value
                    ) for column, value in zip(self.columns, (title, description, datetime, email, status))
                ]
            )

            all_tasks = self.get_task()

            return int(all_tasks[-1][0])
        except Exception as error:
            return str(error)
    
    def update_task(self, id: int, **kwargs):
        values = {column: kwargs.get(column, None) for column in self.columns if kwargs.get(column, None)}
        
        if values:
            if self.get_task_by_id(id=id):
                self.db.update_data(
                    tablename=self.tablename,
                    edit_query=[
                        self.db.ColumnData(
                            column=column,
                            value=value
                        ) for column, value in values.items() if value
                    ],
                    condition=self.db.filter_by(
                        column='id'
                    ).EQUAL(value=id)
                )

                return True

            return False
    
    def get_task(self, status: str = None):
        return self.db.select_data(
            tablename=self.tablename,
            condition=self.db.filter_by(column='status').EQUAL(
                value=status
            ) if status and status.lower() not in ['all'] else None
        )
    
    def get_task_by_id(self, id: int):
        return self.db.select_data(
            tablename=self.tablename,
            condition=self.db.filter_by(column='id').EQUAL(
                value=id
            )
        )

    def delete_data(self, id: int):
        self.db.detele_data(
            tablename=self.tablename,
            condition=self.db.delete_by(
                column='id'
            ).EQUAL(
                value=id
            ) if id else None
        )