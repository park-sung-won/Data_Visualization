from slack_sdk import WebClient
class SlackAlert:
    def __init__(self, channel = '채널명' , token = '토큰' ):
        self.slack_channel = channel
        self.slack_token = token

    def alert( self, context ) :
        client = WebClient(token=self.slack_token)
        text="""
                :red_circle: Task Failed.
                *Task*: {task}  
                *Dag*: {dag}
                *Execution Time*: {exec_date}  
                *Log Url*: {log_url}
                """.format(
                    task=context.get('task_instance').task_id,
                    dag=context.get('task_instance').dag_id,
                    exec_date=context.get('execution_date'),
                    log_url=context.get('task_instance').log_url,
                    )
        response = client.chat_postMessage(channel= self.slack_channel, text= text )
        return response
    def success_alert( self, context ) :
        client = WebClient(token=self.slack_token)
        text="""
                :large_green_circle: Task Success.
                *Task*: {task}  
                *Dag*: {dag}
                *Execution Time*: {exec_date}  
                *Log Url*: {log_url}
                """.format(
                    task=context.get('task_instance').task_id,
                    dag=context.get('task_instance').dag_id,
                    exec_date=context.get('execution_date'),
                    log_url=context.get('task_instance').log_url,
                    )
        response = client.chat_postMessage(channel= self.slack_channel, text= text )
        return response
    
    def image_alert( self , img_dir , comment , file_name = 'temp' ) :
        img = open(img_dir, 'rb').read()
        client = WebClient(token=self.slack_token)
        client.files_upload(
            channels = self.slack_channel,
            initial_comment = comment,
            filename = file_name,
            content = img
        )

        return True
