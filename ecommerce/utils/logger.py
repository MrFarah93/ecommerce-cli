# ecommerce/utils/logger.py
import logging

# Logger setup
logging.basicConfig(
    filename='ecommerce.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
