#ifdef DEBUG
#define DEBUG_PRINT(msg) \
    do { \
        fprintf(stderr, "[DEBUG] %s:%d: %s\n", __FILE__, __LINE__, msg); \
    } while(0)
#else
#define DEBUG_PRINT(msg) ((void)0)
#endif
